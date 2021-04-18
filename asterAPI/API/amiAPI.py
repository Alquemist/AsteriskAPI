import asyncio
from panoramisk import Manager
import json
from pprint import pprint

sipLog = 'sipLog.txt'
manager = Manager(loop=asyncio.get_event_loop(),
                  host='192.168.2.62',
                  username='admin',
                  secret='aster123')

# This will print NewChannel Events.
# AppData='hangupcall, CallerIDName='test2' CallerIDNum='112' Channel='PJSIP/112-0000004a' ChannelState='6',
# ChannelState='6' ChannelStateDesc='Up' ConnectedLineName='Test1' ConnectedLineNum='111' Context='ext-local' Event='Newexten'
#
#
@manager.register_event('Newexten')
def callback(manager, message):
    # resp = yield from manager.send_action({'Action': 'Status'})
    # print(resp)

    state = int(message.get('ChannelState')) if message.get('Application') != 'Hangup' and message.get('Application') != 'Finished' else message.get('Application')

    callStateSwitcher = {
        4: 'Incoming',
        5: 'Ringing',
        6: 'Answered',
        7: 'Busy',
        'Hangup': 'Hangup',
        'Finished': 'NoAnswer',
    }

    sipData = {
        'ChannelState': int(message['ChannelState']),
        'ChannelStateDesc': message['ChannelStateDesc'],
        'CallerIDNum': message['CallerIDNum'],
        'CallerIDName': message['ChannelState'],
        'ConnectedLineNum': message['ConnectedLineNum'],
        'ConnectedLineName': message['ConnectedLineName'],
        'CallState': callStateSwitcher.get(state, 'invalid State'),
    }

    print(sipData, message['Application'])

# # This will print Hangup Events
# @manager.register_event('Hangup')
# def callback(manager, message):
#     print(message)


def main():
    manager.connect()
    try:
        manager.loop.run_forever()
    except KeyboardInterrupt:
        manager.loop.close()


if __name__ == '__main__':
    main()

