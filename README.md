# Notificador de Aulas no WhatsApp

Este é um projeto simples de programação para receber notificações diárias no WhatsApp sobre as aulas agendadas na faculdade.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos antes de começar:

- Python 3 instalado
- Conta no Twilio (para enviar mensagens no WhatsApp)

## Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/notificador-de-aulas.git
   cd notificador-de-aulas
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo de configuração `config.py` com suas credenciais do Twilio:

   ```python
   # config.py
   TWILIO_ACCOUNT_SID = 'sua_account_sid'
   TWILIO_AUTH_TOKEN = 'seu_auth_token'
   TWILIO_PHONE_NUMBER = 'seu_numero_twilio'
   YOUR_PHONE_NUMBER = 'seu_numero_whatsapp'
   ```

   Substitua `'sua_account_sid'`, `'seu_auth_token'`, `'seu_numero_twilio'` e `'seu_numero_whatsapp'` pelos valores corretos obtidos ao criar uma conta no Twilio.

4. Configure as informações de suas aulas no arquivo `aulas.py`:

   ```python
   # aulas.py
   AULAS_DIARIAS = {
       'Segunda-feira': ['Aula de Matemática', 'Aula de História'],
       'Terça-feira': ['Aula de Ciências', 'Aula de Inglês'],
       # Adicione o restante dos dias da semana
   }
   ```

## Execução

Execute o script principal para enviar as notificações:

```bash
python main.py
```

O script enviará automaticamente mensagens no WhatsApp com os detalhes das aulas do dia.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests para melhorar este projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

Este é apenas um exemplo básico. Certifique-se de personalizar as informações de acordo com as necessidades específicas do seu projeto e incluir detalhes adicionais conforme necessário.