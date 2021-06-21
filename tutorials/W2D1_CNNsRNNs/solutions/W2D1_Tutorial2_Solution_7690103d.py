class FMNIST_Net2(nn.Module):
  def __init__(self):
    super(FMNIST_Net2, self).__init__()
    self.conv1 = nn.Conv2d(1, 32, 3, 1)
    self.batch_norm1 = nn.BatchNorm2d(32)
    self.conv2 = nn.Conv2d(32, 64, 3, 1)
    self.batch_norm2 = nn.BatchNorm2d(64)
    self.dropout1 = nn.Dropout(0.5)
    self.dropout2 = nn.Dropout(0.25)
    self.fc1 = nn.Linear(9216, 128)
    self.fc2 = nn.Linear(128, num_classes)

  def forward(self, x):
    x = self.conv1(x)
    x = self.batch_norm1(x)
    x = F.relu(x)
    x = self.conv2(x)
    x = self.batch_norm2(x)
    x = F.relu(x)
    x = F.max_pool2d(x, 2)
    x = self.dropout1(x)
    x = torch.flatten(x, 1)
    x = self.fc1(x)
    x = F.relu(x)
    x = self.dropout2(x)
    x = self.fc2(x)
    return x