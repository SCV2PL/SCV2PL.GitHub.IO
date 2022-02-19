def stop_vm(request):
    from pprint import pprint
    from googleapiclient import discovery
    from oauth2client.client import GoogleCredentials
    
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
    # Project ID for this request.
    project = 'scv2pl' # here you project ID name
    
    # The name of the zone for this request.
    zone = 'europe-central2-a' # put here your zone
    
    # Name of the instance resource to stop.
    instance = 'scv2pl' # put here the name of the vm to start
    req = service.instances().stop(project=project, zone=zone, instance=instance)
    response = req.execute()
