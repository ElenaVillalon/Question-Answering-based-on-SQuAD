# experiment ID
exp = "exp-1"

# data directories
data_dir = "/content/Question-Answering-based-on-SQuAD/SQuAD/"
train_dir = data_dir + "train/"
dev_dir = data_dir + "dev/"

# model paths
spacy_en = "/usr/local/lib/python3.7/dist-packages/spacy/data/en"
glove = "/content/glove.42B.300d.txt"
squad_models = "/content/drive/MyDrive/ProyectoDeepLearningUC/output/" + exp

# preprocessing values
max_words = -1
word_embedding_size = 300
char_embedding_size = 8
max_len_context = 400
max_len_question = 50
max_len_word = 25

# training hyper-parameters
num_epochs = 1
batch_size = 32
learning_rate = 0.5
drop_prob = 0.2
hidden_size = 100
char_channel_width = 5
char_channel_size = 100
cuda = True
#cuda = False
pretrained = False
