# -*- coding:utf-8 -*-
import os
class BaseSaltModule(object):
    def __init__(self,argvs,db_models,settings):
        self.db_models = db_models
        self.sys_argvs = argvs
        self.settings = settings

    def argv_validation(self,argv_name,val,data_type):
        if type(val) is not data_type:
            exit("Error:[%s]'s data type is not valid")



    def get_selected_os_types(self):
        data = {}
        for host in self.host_list:
            data[host.os_type]=[]
        print('--data--',data)
        return data

    def process(self):
        self.fetch_hosts()
        self.config_data_dic = self.get_selected_os_types()

    def fetch_hosts(self):

        print('fetching the host')
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h')+1
                if len(self.sys_argvs) <= host_str_index:
                    exit('host argvment must fi')
                else:
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list)
                    print('-----host_list:',host_list)
            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g') + 1
                if len(self.sys_argvs) <= group_str_index:
                    exit('group argument must be pro after -g')
                else:
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    print('333',group_str_list)
                    group_list = self.db_models.Group.objects.filter(name__in=group_str_list)
                    for group in group_list:
                        host_list += group.hosts.select_related()
            print('----group',host_list)
            self.host_list = set(host_list)
            print('---jing--',self.host_list)
        else:
            exit('host [-h] or group [-g] must be provided')

    def syntax_parser(self,section_name,mod_name,mod_data,os_type):
        print('?????',section_name)
        print('--going to parser state data',)
        self.raw_cmds = []
        self.single_line_cmds = []
        for state_item in mod_data:
            print '\t',state_item
            for key,val in state_item.items():
                if hasattr(self,key):
                    state_fun = getattr(self,key)
                    state_fun(val,section=section_name,os_type=os_type)
                else:
                    exit('Error,module [%s] has no argument [%s]'%(mod_name,key))
        else:
            if '.' in mod_name:
                base_mod_name,mod_action = mod_name.split('.')
                if hasattr(self,mod_action):
                    mod_action_func = getattr(self,mod_action)
                    cmd_list = mod_action_func(section=section_name)
                    data = {
                        'cmd_list':cmd_list,
                        'required_list':self.require_list
                    }#代表一个section里具体的一个module已经解析完毕
                    return data


    def is_required(self,*args,**kwargs):
        exit('Error:is_required method must be implment in each method [%s]'%args[0])

    def require(self,*args,**kwargs):
        os_type = kwargs.get('os_type')
        print("in require..",args,kwargs)
        self.require_list =[]
        for item in args[0]:
            for mod_name,mod_val in item.items(): #pkg:apache
                module_obj = self.get_module_instance(base_mod_name=mod_name,os_type=os_type)
                require_condition = module_obj.is_required(mod_name,mod_val)
                print('9999require run module..',module_obj)
                self.require_list.append(require_condition)




    def get_module_instance(self,*args,**kwargs):
        base_mod_name = kwargs.get('base_mod_name')
        os_type = kwargs.get('os_type')
        plugin_file_path = "%s/%s.py" % (self.settings.SALT_PLUGINS_DIR, base_mod_name)
        if os.path.isfile(plugin_file_path):  # j导入模块
            module_plugin = __import__('plugins.%s' % base_mod_name)
            special_os_module_name = "%s%s" % (os_type.capitalize(), base_mod_name.capitalize())
            print('dir-module-plugin', module_plugin)  # 这里是将这个文件夹里面的__init__导入，
            # ('dir-module-plugin', <module 'plugins' from 'G:\workgroup\oldboyProject\Arya\plugins\__init__.pyc'>)
            module_file = getattr(module_plugin, base_mod_name)  # 这里是加载plugins目录下面的各个方法反射过来，请看下面的路径
            print('222', module_file)
            # ('222', <module 'plugins.user' from 'G:\workgroup\oldboyProject\Arya\plugins\user.pyc'>)
            if hasattr(module_file, special_os_module_name):
                module_instance = getattr(module_file, special_os_module_name)  # 这里相当于是打开user.py里面的文件寻找User的类
            else:
                module_instance = getattr(module_file, base_mod_name.capitalize())
                print('333',module_instance)
                # 开始在plugins调用对面的module进行配置解析
                module_obj = module_instance(self.sys_argvs, self.db_models, self.settings)
                print('4444',module_obj)
                return module_obj
        else:
            exit('module [%s] is not existed' % base_mod_name)
            # for state_item in mod_data:
            #     print '\t',state_item
