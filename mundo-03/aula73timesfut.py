times = ("Flamengo", "Santos","Palmeiras","Grêmio","Athlético-PR","São Paulo","Internacional","Corinthians","Fortaleza",
         "Goiás","Bahia","Vasco","Atlético-MG","Fluminense","Botafogo","Ceará","Cruzeiro","CSA","Chapecoense","Avaí")
print(f"Lista de times do Brasileirão 2019: {times}")
print("=-="*30)
print(f"Os 5 primeiros foram: {times[:5]}")
print("=-="*30)
print(f"Os 4 últimos foram: {times[-4:]}")
print("=-="*30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("=-="*30)
print(f"O Flamengo ficou em {times.index("Flamengo")+1}º.")