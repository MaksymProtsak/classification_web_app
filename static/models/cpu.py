import tensorflow as tf

model = tf.keras.models.load_model("save_at_49.keras", compile=False)
model.compile()  # Компільовуємо для CPU
model.save("save_at_49_cpu.keras")  # Зберігаємо новий варіант