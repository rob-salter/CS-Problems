class BufferFullException(BufferError):
  """Exception raised when CircularBuffer is full.

  message: explanation of the error.

  """
  def __init__(self, message):
      self.message = message


class BufferEmptyException(BufferError):
  """Exception raised when CircularBuffer is empty.

  message: explanation of the error.

  """
  def __init__(self, message):
      self.message = message


class CircularBuffer:
  def __init__(self, capacity):
      self.capacity = capacity
      self.buffer = []
    
  def read(self):
      if len(self.buffer) == 0:
          raise BufferEmptyException("Circular buffer is empty")
      return self.buffer.pop(0)

  def write(self, data):
      if len(self.buffer) == self.capacity:
        raise BufferFullException("Circular buffer is full")
      self.buffer.append(data)

  def overwrite(self, data):
      if len(self.buffer) == self.capacity:
          self.buffer = self.buffer[1:]
      self.buffer.append(data)

  def clear(self):
      self.buffer = []


buf = CircularBuffer(1)
buf.write("1")
#buf.write("2")
print(buf.read())
# buf.write("3")
print(buf.read())
# buf.clear()
# print(buf.read())
# #buf.clear()