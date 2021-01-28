import os
from keras_bert import get_model
inputs, outputs = get_model(
    token_num=len(token_dict),
    head_num=5,
    transformer_num=12,
    embed_dim=25,
    feed_forward_dim=100,
    seq_len=20,
    pos_num=20,
    dropout_rate=0.05,
    training=False,
)

flatten=keras.layers.Flatten()(outputs)
finaloutput=keras.layers.Dense(units=1, activation='sigmoid')(flatten)
model=keras.models.Model(inputs,finaloutput)
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
model.fit([trainpos,trainseg],trainy,batch_size=128,epochs=20)
