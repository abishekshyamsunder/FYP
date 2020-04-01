messages = ["Page load times are slow",
"Fix node assignments not not allow slaves on master.",
"Speed up page load/reload times",
"Support Resume For Add Nodes",
"Fix puppet manifests for tarball downloads via rpms.",
"Fix Advanced Config: HDFS reserved space is in bytes. Too many bytes to count.",
"Create a spec file with less dependencies for HMC",
"Puppet fails to install 32-bit JDK properly on RHEL6",
"Change os type check during node bootstrap to allow RHEL6 or CentOS6 nodes",
"Puppet agent install script should use correct epel repo",
"Add support to jump to a specified state in the wizard for development purposes",
"Update README to point to trunk",
"Remove YUI source files from SVN",
"Nagios install fails on RHEL6",
"In Custom config for Nagios: emails with multiple periods before the '@' fails validation",
"Custom Config page: don't allow form submission if there are client-side validation errors",
"HDFS disk capacity on dashboard is seen as negative number",
"Host component live status is broken",
"dashboard > Summary > capacity pie chart keeps changing colors",
"License header for PHP files should use PHP comments  not HTML comments",
"Add a link to NOTICE file on every page",
"Fix lzo installs to work correctly on RHEL6",
"Increase puppet timeouts to handle single-node installs timing out",
"Eliminate redundant and unused definition for the columns in the table ConfigProperties",
"Make puppet generate more logs on command failures",
"Ambari should install yum priorities on all nodes to ensure main repo is picked first",
"Create heatmap legend entries for missing data/invalid hosts",
"Need to be able to reliably recover from the case when the browser is closed during deploy (Step 8 post submission  Step 9) of the wizard",
"User-specified custom configs (such as hdfs-site.xml overrides) should be persisted to maintain what the user specified",
"On Notification Popup  clicking 'go to nagios UI' doesn't load nagios UI",
"Error handling when errors are encountered during preparation for deploy",
"Account not locking after multiple invalid logins",
"application is not redirecting to website",
"the classifier's accuracy is very low",
"the load time for the application is too high",
"the browser is not opening when clicked",
"The interface submits with many field filled incorrectly",
"character limit for name should be increased",
]
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