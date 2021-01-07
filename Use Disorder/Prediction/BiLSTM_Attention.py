def attention_3d_block(inputs):
    # inputs.shape = (batch_size, time_steps, input_dim)
    input_dim = int(inputs.shape[2])
    a = Permute((2, 1))(inputs)
    a = Reshape((input_dim, TIME_STEPS))(a) # this line is not useful. It's just to know which dimension is what.
    a = Dense(TIME_STEPS, activation='softmax')(a)
    if SINGLE_ATTENTION_VECTOR:
        a = Lambda(lambda x: K.mean(x, axis=1), name='dim_reduction')(a)
        a = RepeatVector(input_dim)(a)
    a_probs = Permute((2, 1), name='attention_vec')(a)
    output_attention_mul = Multiply()([inputs, a_probs])
    return output_attention_mul

S_inputs = Input(shape=(trainx.shape[1],trainx.shape[2],))
attention_mul = attention_3d_block(S_inputs)
O_seq = Attention(16,16)([attention_mul,attention_mul,attention_mul])
O_lstm = Bidirectional(LSTM(512, return_sequences=False))(O_seq)
outputs = Dense(1, activation='sigmoid')(O_lstm)
trans = Model(inputs=S_inputs, outputs=outputs)
trans.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
trans.fit(trainx,trainy,epochs=20,batch_size=64)
