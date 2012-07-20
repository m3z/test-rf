# -*- coding: utf-8 -*-

import command as cmd
import topologyParser
import heapq
import pickle


isDebug = True;


openflowSwitchList = ['switch0','switch1']
openflowSwitchDict = {'switch0':0,'switch1':0}

#重启后清除flowvisor的内容
def cleanAll():
        cmd.runFlowVisor()
        time.sleep(2)
        cmd.cleanSlices()
        cmd.cleanFlowSpace()

#启动ovs
def startOVS():

       # dictFile = open('/switchDict','wb')
       # pickle.dump(openflowSwitchDict,dictFile)
       # dictFile.close()

	for openflowSwitch in openflowSwitchList:
		cmd.ovsOpenflowd(openflowSwitch, '127.0.0.1', 6633)
	


if __name__ == '__main__':
        cleanAll()
        startOVS()
