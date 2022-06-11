import buildhat

distance_sensor_f = buildhat.DistanceSensor('C')
distance_sensor_s = buildhat.DistanceSensor('D')

print(distance_sensor_f.get_distance())
print(distance_sensor_s.get_distance())