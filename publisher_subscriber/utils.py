import redis

# redis_instance = redis.StrictRedis(host='aerios-ec-dqu.3mvwix.0001.use1.cache.amazonaws.com', port=9000, db=0)

redis_instance = redis.StrictRedis()
pub_sub = redis_instance.pubsub()


def publisher(channel, message):

    response = redis_instance.publish(channel, message)
    return response


def subscriber(channel):

    pub_sub.subscribe(channel)
    response = pub_sub.get_message()
    return response


def unsubsciber(channel):

    response = pub_sub.unsubscribe(channel)
    return response


def listen_message():

    messages = []
    for message in pub_sub.listen():
        print(message)
        messages.append(message)

    return messages


# print(subscriber("otp_channel"))
# print(publisher("otp_channel", "Your otp is 12345"))
# print(listen_message())
# print(unsubsciber(channels))