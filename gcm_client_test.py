# coding=utf-8
from gcm import GCM
import config

gcm = GCM(config.params['API_KEY'])
#data = {'param1': 'value1', 'param2': 'value2', 'message':'Hello world!'}

data = {
    'id': config.params['id'],
    'report_id': config.params['report_id'],
    'user_id': config.params['user_id'],
    'expert_id': config.params['expert_id'],
    'date_comment': config.params['date_comment'],
    'expert_comment': config.params['expert_comment'],
    'expert_html': config.params['expert_html'],
    'photo_url': config.params['photo_url'],
    'acknowledged': config.params['acknowledged']
}

# Downstream message using JSON request
reg_ids = [config.params['REG_ID']]
response = gcm.json_request(registration_ids=reg_ids, data=data)

# Downstream message using JSON request with extra arguments
res = gcm.json_request(
    registration_ids=reg_ids, data=data,
    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
)

# Topic Messaging
# topic = 'topic name'
# gcm.send_topic_message(topic=topic, data=data)