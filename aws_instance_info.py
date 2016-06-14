import boto.ec2
import json
import sys
ec2 = boto.ec2.connect_to_region('us-east-1')

#reservations= ec2.get_all_instances(filters={'tag:krole': 'npe'})
reservations= ec2.get_all_instances()
#print instances

for reservation in reservations:
	instances = reservation.instances
	for instance in instances:
		name = ec2.get_all_tags(filters={'resource-id': instance.id, 'key':'Name'})[0].value
		#if name[ :2] == "st":
		print name,":",instance.instance_type,":",instance.id,":",instance.private_ip_address
