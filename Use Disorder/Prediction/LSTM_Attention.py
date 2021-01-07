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

def model_attention_applied_before_lstm(n):
    K.clear_session() #清除之前的模型，省得压满内存
    inputs = Input(shape=(TIME_STEPS, INPUT_DIM,))
    attention_mul = attention_3d_block(inputs)
    lstm_units = n
    attention_mul = LSTM(lstm_units, return_sequences=False)(attention_mul)
    output = Dense(1, activation='sigmoid')(attention_mul)
    model = Model([inputs], output=output)
    return model

def model_attention_applied_before_lstm2(n,m):
    K.clear_session() #清除之前的模型，省得压满内存
    inputs = Input(shape=(TIME_STEPS, INPUT_DIM,))
    attention_mul = attention_3d_block(inputs)
    lstm_units = n
    attention_mul = LSTM(n, return_sequences=True)(attention_mul)
    attention_mul2 = LSTM(m, return_sequences=False)(attention_mul)
    output = Dense(1, activation='sigmoid')(attention_mul2)
    model = Model(input=[inputs], output=output)
    return model

ls22i=model_attention_applied_before_lstm(512，512)
ls22i.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
ls22i.fit(trainx3,trainy2,epochs=10,batch_size=256,verbose=1)

