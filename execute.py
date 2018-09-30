# import setup_path 
import airsim
import time
import numpy as np
import os
import pprint
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

print("Taking OFF")
client.takeoffAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

print("Moving to position")
client.moveToPositionAsync(0, 0, -50, 10).join()

# for i in points:
# -42.003983	-28.115284	-50.316597
# -48.902599	52.301170	-50.129326
# 44.438919	20.640558	-51.753590
# x=-42
# y=-28
# z=-50

points = np.array([-42.003983,-28.115284,-50.316597,-1,-48.902599,52.301170,-50.129326,-3,50.438919,21.640558,-51.753590,-2])
points = np.reshape(points,(3,4))
# points = np.array([50.438919,21.640558,-51.753590,-48.902599,52.301170,-50.129326])
# points = np.reshape(points,(2,3))
for i in points:
	print(i)
	x = int(i[0])
	y = int(i[1])
	z = int(i[2])
	h = int(i[3])
	print("Moving to position")
	client.moveToPositionAsync(x, y, z, 10).join()

	print("Hovering")
	client.hoverAsync().join()

	print("Killing mosquitoes")
	client.moveToPositionAsync(x, y, h, 10).join()

	print("Hovering")
	client.hoverAsync().join()

	time.sleep(2)

	state = client.getMultirotorState()
	print("state: %s" % pprint.pformat(state))

	print("Moving to position")
	client.moveToPositionAsync(x, y, z, 10).join()

print("flying back home")
client.moveToPositionAsync(0, 0, z, 10).join()

print("landing...")
client.landAsync().join()

client.armDisarm(False)
client.reset()
# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
