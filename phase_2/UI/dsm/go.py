def go_function():
    import tensorflow_hub as hub
    import numpy as np
    import tensorflow.compat.v1 as tf
    tf.disable_eager_execution()
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"
    print("Program Started")

    # Import the Universal Sentence Encoder's TF Hub module
    embed = hub.Module(module_url)

    # sample text

    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_message_encodings = embed(similarity_input_placeholder)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: messages})

        corr = np.inner(message_embeddings_, message_embeddings_)
        temp1 = 0
        temp2 = 0
        jtemp = 0
        for j in range(len(messages)-1):
            temp = max(corr[0][j+1],temp2)
            if temp>temp2:
                jtemp=j+1
                temp2=temp
        print(corr)
        print(messages[jtemp] + "\n" + messages[0])
        #f = open('temp.temp','w')
        #f.write('SIMILAR ISSUE FOUND: '+messages[jtemp])
        #f.close()
        return 'SIMILAR ISSUE FOUND: '+messages[jtemp]
        #heatmap(messages, messages, corr)