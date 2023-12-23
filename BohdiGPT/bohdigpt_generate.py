import numpy
import tensorflow as tf
import random
import json
import pickle


with open('intents.json', encoding="utf8" ) as file:
    data = json.load(file)
    
max_len = 10
sequences = []
seq_y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sequences.append(pattern)
        seq_y.append(intent["tag"])

num_classes = len(set(seq_y))
training = numpy.array(sequences)
y_train = numpy.array(seq_y)
y_train = y_train -1
#todo confirm if max_len is needed
vectorize_layer = tf.keras.layers.TextVectorization(
    output_mode='int',
    output_sequence_length= max_len
)
vectorize_layer.adapt(training)

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(1,), dtype=tf.string))
model.add(vectorize_layer)
model.add(tf.keras.layers.Embedding(input_dim=len(vectorize_layer.get_vocabulary()), output_dim=50, input_length=max_len))
model.add(tf.keras.layers.LSTM(64))
model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training, y_train, epochs=10, batch_size=1, validation_split=0.2)

model.save("bohdiGPT.model")

#converter = tf.lite.TFLiteConverter.from_keras_model(model)
#converter.optimizations = [tf.lite.Optimize.DEFAULT]
#converter._experimental_lower_tensor_list_ops = False
#converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
#tf.lite.OpsSet.SELECT_TF_OPS]
#tflite_model = converter.convert()

#with open('bohdiGPT_model.tflite', 'wb') as f:
#    f.write(tflite_model)