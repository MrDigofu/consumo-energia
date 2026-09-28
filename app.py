def obter_numero_valido(mensagem, minimo=0, permitir_zero=True):
    """
    Obtém um número válido do usuário com validação.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo or (valor == 0 and not permitir_zero):
                print(f"❌ Erro: Digite um valor maior que {minimo}.")
                continue
            return valor
        except ValueError:
            print("❌ Erro: Digite apenas números válidos.")


def adicionar_aparelho():
    """
    Adiciona um novo aparelho ao cálculo.
    """
    print("\n" + "=" * 50)
    print("➕ ADICIONAR NOVO APARELHO")
    print("=" * 50)
    
    aparelho = input("Digite o nome do aparelho: ").strip()
    if not aparelho:
        print("❌ Nome não pode estar vazio.")
        return None
    
    potencia = obter_numero_valido(
        f"Potência do {aparelho} em Watts (W): ", 
        minimo=0, 
        permitir_zero=False
    )
    
    horas_dia = obter_numero_valido(
        f"Tempo médio de uso diário (horas): ", 
        minimo=0, 
        permitir_zero=True
    )
    
    return {
        "nome": aparelho,
        "potencia": potencia,
        "horas_dia": horas_dia
    }


def calcular_consumo(aparelhos, valor_kwh=0.75):
    """
    Calcula o consumo e custo mensal para todos os aparelhos.
    """
    resultados = []
    consumo_total = 0
    custo_total = 0
    
    for aparelho in aparelhos:
        consumo_mensal = (aparelho["potencia"] * aparelho["horas_dia"] * 30) / 1000
        custo_mensal = consumo_mensal * valor_kwh
        
        consumo_total += consumo_mensal
        custo_total += custo_mensal
        
        resultados.append({
            "nome": aparelho["nome"],
            "potencia": aparelho["potencia"],
            "horas_dia": aparelho["horas_dia"],
            "consumo_mensal": consumo_mensal,
            "custo_mensal": custo_mensal,
            "percentual": 0  # Calculado depois
        })
    
    # Calcular percentual de cada aparelho
    if consumo_total > 0:
        for resultado in resultados:
            resultado["percentual"] = (resultado["consumo_mensal"] / consumo_total) * 100
    
    return resultados, consumo_total, custo_total


def exibir_resultados(resultados, consumo_total, custo_total, valor_kwh):
    """
    Exibe os resultados de forma formatada e visual.
    """
    print("\n" + "=" * 70)
    print("📊 RESULTADO DO CONSUMO ELÉTRICO")
    print("=" * 70)
    
    print(f"\n{'APARELHO':<20} {'POTÊNCIA':<12} {'HORAS/DIA':<12} {'CONSUMO/MÊS':<15} {'CUSTO/MÊS':<12}")
    print("-" * 70)
    
    for r in resultados:
        print(f"{r['nome']:<20} {r['potencia']:>10.1f} W {r['horas_dia']:>10.1f} h "
              f"{r['consumo_mensal']:>12.2f} kWh {r['custo_mensal']:>11.2f} R$")
    
    print("-" * 70)
    print(f"{'TOTAL':<20} {'':<12} {'':<12} {consumo_total:>12.2f} kWh {custo_total:>11.2f} R$")
    print("=" * 70)
    
    print(f"\n💡 DETALHAMENTO POR APARELHO:")
    print("-" * 70)
    
    for r in resultados:
        print(f"\n🔌 {r['nome'].upper()}")
        print(f"   Potência: {r['potencia']:.1f} W")
        print(f"   Uso diário: {r['horas_dia']:.1f} horas")
        print(f"   Consumo mensal: {r['consumo_mensal']:.2f} kWh")
        print(f"   Custo mensal: R$ {r['custo_mensal']:.2f}")
        print(f"   Percentual do total: {r['percentual']:.1f}%")
    
    print("\n" + "=" * 70)
    print(f"⚡ RESUMO FINAL")
    print("=" * 70)
    print(f"Consumo total mensal: {consumo_total:.2f} kWh")
    print(f"Custo total mensal: R$ {custo_total:.2f}")
    print(f"Custo médio por kWh: R$ {valor_kwh:.2f}")
    print(f"Custo anual estimado: R$ {custo_total * 12:.2f}")
    print("=" * 70)


def menu_principal():
    """
    Exibe o menu principal e controla o fluxo do programa.
    """
    print("\n" + "=" * 50)
    print("⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")
    print("=" * 50)
    
    aparelhos = []
    valor_kwh = 0.75
    
    while True:
        print("\n📋 MENU PRINCIPAL")
        print("-" * 50)
        print("1️⃣  Adicionar aparelho")
        print("2️⃣  Alterar valor do kWh (atual: R$ {:.2f})".format(valor_kwh))
        print("3️⃣  Calcular e exibir resultados")
        print("4️⃣  Limpar lista de aparelhos")
        print("5️⃣  Sair")
        print("-" * 50)
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            novo_aparelho = adicionar_aparelho()
            if novo_aparelho:
                aparelhos.append(novo_aparelho)
                print(f"✅ {novo_aparelho['nome']} adicionado com sucesso!")
                print(f"   Total de aparelhos: {len(aparelhos)}")
        
        elif opcao == "2":
            valor_kwh = obter_numero_valido(
                "Digite o novo valor do kWh (R$): ",
                minimo=0,
                permitir_zero=False
            )
            print(f"✅ Valor do kWh atualizado para R$ {valor_kwh:.2f}")
        
        elif opcao == "3":
            if not aparelhos:
                print("❌ Nenhum aparelho adicionado. Adicione pelo menos um aparelho.")
                continue
            
            resultados, consumo_total, custo_total = calcular_consumo(aparelhos, valor_kwh)
            exibir_resultados(resultados, consumo_total, custo_total, valor_kwh)
        
        elif opcao == "4":
            if aparelhos:
                aparelhos.clear()
                print("✅ Lista de aparelhos limpa com sucesso!")
            else:
                print("ℹ️  A lista já estava vazia.")
        
        elif opcao == "5":
            print("\n👋 Obrigado por usar a Calculadora de Consumo Elétrico!")
            print("=" * 50)
            break
        
        else:
            print("❌ Opção inválida. Digite um número entre 1 e 5.")


if __name__ == "__main__":
    menu_principal()
