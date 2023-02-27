faturamento_diario = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

valor_minimo = faturamento_diario[0]['valor']
dia_valor_minimo = None
valor_maximo = faturamento_diario[0]['valor']
dia_valor_maximo = None
somatorio = 0
for dic in faturamento_diario:
    if dic['valor'] == 0:
        continue
    else:
        somatorio += dic['valor']
        if dic['valor'] < valor_minimo:
            valor_minimo = dic['valor']
            dia_valor_minimo = dic['dia']
        if dic['valor'] > valor_maximo:
            valor_maximo = dic['valor']
            dia_valor_maximo = dic['dia']
media = somatorio / len(faturamento_diario)
print(f'O valor mínimo de faturamento diário registrado no mês foi de {valor_minimo} e ocorreu no dia {dia_valor_minimo}.')
print(f'O valor máximo de faturamento diário registrado no mês foi de {valor_maximo} e ocorreu no dia {dia_valor_maximo}.')
print(f'O valor médio de faturamento diário registrado no mês foi de %.4f' %media)

acima_media = []
for dic in faturamento_diario:
    if dic['valor'] == 0:
        continue
    else:
        if dic['valor'] > media:
            acima_media.append(dic['valor'])
print(f'No toral, {len(acima_media)} dias no mês registramento faturamento diário superior à média mensal.')