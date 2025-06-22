import zipfile
import os
import tensorflow as tf
import datetime
import matplotlib.pyplot as plt
def unzip_data(file_path, extract_to='.'):
    """
    Unzips the specified zip file to the given directory.
    
    :param file_path: Path to the zip file.
    :param extract_to: Directory to extract files to. Defaults to current directory.
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def walk_directory(directory):
    """
    Walks through the specified directory and returns a list of all files.
    
    :param directory: Directory to walk through.
    :return: List of file paths.
    """
    for dirpath, dirnames, files in os.walk(directory):
        print(f'There are {len(files)} files and {len(dirnames)} directories in {dirpath}')

def create_tensorboard_callback(dir_name, experiment_name):
  log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
  tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir)
  print(f"Saving TensorBoard log files to: {log_dir}")
  return tensorboard_callback

def plot_loss_curves(history):
  """
  Returns seperate loss curves for training and validation metrics.
  """
  loss = history.history["loss"]
  val_loss = history.history["val_loss"]

  accuracy = history.history["accuracy"]
  val_accuracy = history.history["val_accuracy"]

  epochs = range(len(history.history["loss"]))

  plt.plot(epochs, loss, label = "training loss")
  plt.plot(epochs, val_loss, label = "val_loss")
  plt.title("loss")
  plt.xlabel("epochs")
  plt.legend()

  plt.figure()
  plt.plot(epochs, accuracy, label = "training_acuracy")
  plt.plot(epochs, val_accuracy, label = "val_accuracy")
  plt.title("accuracy")
  plt.xlabel("epochs")
  plt.legend()