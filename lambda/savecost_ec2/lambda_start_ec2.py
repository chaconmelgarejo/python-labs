import boto3
import logging

# log setuṕ
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# boto connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    # define the filters to help us to start & stop using tag
    filters = [ { 'Name': 'tag:stateOff' , 'Values': ['atnight'] },
                { 'Name': 'instance-state-name', 'Values': ['stopped'] }
    ]

    # save the instances matched
    instances = ec2.instances.filter(Filters=filters)

    # saves all stopped instances
    isStopped = [instance.id for instance in instances]

    # start each instance that are stopped
    if len(isStopped) > 0:
        startingUp = ec2.instances.filter(InstanceIds=isStopped).start()
        print (startingUp)
    else:
        print ("Good Job!")
