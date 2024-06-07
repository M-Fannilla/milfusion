import torch
import torch.nn as nn
import torch.optim as optim
from vit_pytorch import ViT
from sklearn.metrics import f1_score
from efficientnet_pytorch import EfficientNet
from transformers import ViTForImageClassification, ViTConfig


class WeightedBinaryCrossEntropyLoss(nn.Module):

    def __init__(self, weights):
        super(WeightedBinaryCrossEntropyLoss, self).__init__()
        self.weights = weights
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def forward(self, logits, targets):
        logits = torch.sigmoid(logits)
        bce = nn.BCELoss(reduction='none')(logits, targets)
        weighted_bce = bce * self.weights
        return weighted_bce.mean()


def weighted_binary_cross_entropy(output, target, weights):
    loss = nn.BCEWithLogitsLoss(reduction='none')(output, target)
    loss = loss * weights
    return loss.mean()


def calculate_metrics(outputs, labels):
    outputs = torch.sigmoid(outputs).cpu().detach().numpy()
    labels = labels.cpu().detach().numpy()

    # Calculate micro-average F1-score
    micro_f1 = f1_score(labels, outputs.round(), average='micro')

    return micro_f1


class MultiLabelEfficientNet(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.model = EfficientNet.from_pretrained('efficientnet-b7')
        self.model._fc = nn.Linear(self.model._fc.in_features, num_classes)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def forward(self, x):
        x = self.model(x)
        return x


class MultiLabelViT(nn.Module):
    def __init__(self, image_size, num_classes):
        super().__init__()
        self.vit = ViT(
            image_size=image_size,
            patch_size=32,
            num_classes=num_classes,
            dim=1024,
            depth=6,
            heads=16,
            mlp_dim=2048,
            dropout=0.1,
            emb_dropout=0.1
        )

    def forward(self, x):
        return self.vit(x)


class HFViT(nn.Module):
    def __init__(self, num_classes, model_name='google/vit-large-patch32-384'):
        super().__init__()
        self.config = ViTConfig.from_pretrained(model_name)
        self.config.num_labels = num_classes
        self.model = ViTForImageClassification.from_pretrained(model_name, config=self.config)

        # Replace the classifier head
        self.model.classifier = nn.Linear(self.config.hidden_size, num_classes)

    def forward(self, x):
        return self.model(x).logits


def train_model(model: nn.Module, dataloader, class_weights):
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 10
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0

        for inputs, labels in dataloader:
            inputs, labels = inputs.to(model.device), labels.to(model.device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = weighted_binary_cross_entropy(outputs, labels, class_weights)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {running_loss / len(dataloader)}')

    print('Training finished.')
