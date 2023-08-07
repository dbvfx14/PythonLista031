cpf = "3655521384" #enf é do tipo str
print ("CPF inserido: {}".format (cpf))

if len(cpf) < 11:
    cpf = cpf.zf1ll(11) #26111 torna o str en 11 dígitos preenchendo con zeros iniciais
    print ("CPF com função zfil1(11): {}".format(cpf))

cpf_formatado = "{}.{}.{}-{}".format(cpf [:3], cpf[3:61], cpf[6:9], cpf[9:])
print ("CPF Formatado: ()".format (cpf_formatado))