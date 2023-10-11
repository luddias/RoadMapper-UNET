import json
from tensorflow.keras.utils import to_categorical
import pandas as pd
import numpy as np
from tqdm import tqdm

"""
2353 imagens de cada uma das 16 primeiras classes
2352 imagens da classe 17
"""

def test_data_generator(pos_ini, nrows):
    test_df = "csv_datasets/dataset_teste_50K_10K.csv" #

    df = pd.read_csv(
                    test_df, skiprows=pos_ini, nrows=nrows, header=None)
    df.dropna()
    y = []
    for i in range(0, len(df)):
        try:
            y.append(json.loads(df.iloc[i,1]))
        except:
            df.drop(i, axis=0, inplace=True)
            print("Linha inválida removida")

    df.to_csv('dataset_treino_50K_10K_novo.csv', index=False, header=False, mode="a") #
    y = np.asarray(y)
    
    return y

def classes_in_array(dado):   
    quant_class = np.zeros(17, dtype = np.uint8)
    for lin in dado:
        for v in lin:
            d = v[0]
            for i in range(17):
                if d==i:
                    quant_class[i]=1
    return quant_class
                        
def classes_dic():
    dic = {}
    for i in range(17):
        dic[i] = 0
    
    return dic

def update_classes(classes, quant_classes):
    for i in range(len(quant_classes)):
        if quant_classes[i]>0:
            classes[i]+=1
    
def main():
    classes = classes_dic()
    n_imgs = 10000 #
    tam_lote=500 #
    n_lotes = int(n_imgs/tam_lote)
    for n in tqdm(range(0, n_lotes), desc="Processing..."):
        dados = test_data_generator(n*tam_lote, nrows=tam_lote)
        for dado in dados: # dado = array de uma imagem
            quant_classes = classes_in_array(dado)
            update_classes(classes, quant_classes)

    print(classes)
            
main()