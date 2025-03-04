import torch
import torch.nn as nn
import torch.optim as optim



class CombinedCNN(nn.Module):
    def __init__(self, extractor, classifier):
        super(CombinedCNN, self).__init__()
        self.extractor = extractor
        self.classifier = classifier
        
    def forward(self, x):
        x = self.extractor(x)
        x = self.classifier(x)
        
        return x

def train_model_CNN(feature_extractor, classifier, train_loader, train_labels , num_epochs, learning_rate):
    model = CombinedCNN(feature_extractor, classifier)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for i in range(len(train_loader)):

            outputs = model(train_loader[i])
            loss = criterion(outputs, train_labels[i])

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            print('Epoch:', epoch, ', Loss:', loss.item())

    print("Training complete.")
    return model



def supervised_transformer(model, train_loader, train_labels, num_epochs, learning_rate):
    criterion_total = nn.MSELoss()
    criterion_dist = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters, lr = learning_rate)
    