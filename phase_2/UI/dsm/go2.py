messages = ["Page load times are slow",
"the account should be locked after 3 invalid login attempts",
"the application must redirect to website after 10 seconds",
"the classifier must give an accuracy upward of 80 percent.",
"slaves should not be permitted on master",
"load time should be less than 10 seconds",
"Add nodes should support Resume",
"The interface must have 5 fields to be filled correctly",
"The browser should open within 5 seconds of clicking ",
"The CPU must clock atleast 10 cycles per minute",
"tarball downloads via rpms should be supported ",
"HDFS reserved space should be displayed in kilo bytes",
"Number of HMC dependencies should be low",
"Puppet should support 32 bit JDK installation on RHEL6",
"Node bootstrap should allow RHEL6 and CentOS6 nodes",
"Puppet agent install script should use latest epel repository",
"Functionality to jump to a specified state in the wizard should be provided",
"README should point to trunk",
"The interface must have 5 fields to be filled correctly",
"The browser should open within 5 seconds of clicking ",
"The CPU must clock atleast 10 cycles per minute",
"The function should not be called if one parameter is missing",
"SVN should not contain any YUI files",
"RHEL6 should support Nagios installation",
"Any format of email should be accepted by Nagios",
"User should be allowed to submit the form only if there are no errors",
"HDFS disk capacity should be a whole number only",
"Display host component's live status on the homepage",
"All pie charts in the application should be blue",
"License header for php files should use php comments",
"Every page should be linked to Notice file",
"RHEL6 should support lzo installs",
"The interface must have 5 fields to be filled correctly",
"The browser should open within 5 seconds of clicking ",
"The CPU must clock atleast 10 cycles per minute",
"The function should not be called if one parameter is missing",
"Puppet should not timeout before single node installation is completed",
"There should be no repeating columns in any of the tables",
"Puppet should generate detailed logs on command failures",
"yum priorities should be installed on all nodes",
"Missing data should have heatmap entries",
"Recovery should be smooth and easy when browser crashes during deploy.",
"User-specified configs should not be overwritten",
"Nagios UI should be loaded when the popup is clicked",
"Handle errors when they are encountered during deploy",
"Data must be entered before a request can be approved.",
"The system will limit access to authorized users.",
"Members of the Data Entry group can enter requests but can not approve or delete requests.",
"All personnel using the system will be trained according to internal SOP AA-101",
"Field 1 should accept only numeric data entry",
"Data secured with an electronic signature cannot be edited or deleted unless the electronic signature is removed",
"User passwords will expire after a certain period of time, in according with Ofni Systems rules or a system administration SOP.",
"Protection of records to enable their accurate and ready retrieval throughout the records retention period.",
"Include the Date/Time when the electronic signature was applied when generated.",
"Users are able to view resulting data on a standard report created by the developer for the search being use",
"The diplay should become 42 nits at sundown",
"battery saver should be switched on if battery falls below 5%",
"The name can\'t exceed 5 characters",
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