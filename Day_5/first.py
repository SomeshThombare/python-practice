#how to check the preloaded moduel and there counts
import sys
print('total moduel loaded : ', len(sys.modules))
for module_name in list(sys.modules.keys())[ :10] :
    print(module_name)