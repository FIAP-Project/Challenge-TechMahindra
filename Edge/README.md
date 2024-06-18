Pedro Henrique Martins Alves dos Santos RM: 558107

Victor de Almeida Gonçalves RM: 558799

Felipe Cerboncini Cordeiro RM: 554909

Matheus Rezende RM: 559190

Projeto: Sistema de Segurança

Descrição: 

Este projeto utiliza um Arduino para monitorar a distância com um sensor ultrassônico (HC-SR04) e a aceleração com um acelerômetro MPU6050. O objetivo é alertar sobre possíveis colisões ou riscos durante o uso.

Funcionalidades: 

1. Monitoramento de Distância:

- Utiliza o sensor ultrassônico HC-SR04 para medir a distância entre o veículo (ou objeto monitorado) e obstáculos próximos.
- Quando a distância medida está entre 0 e 50 cm, o buzzer é acionado para indicar proximidade perigosa, acima disso é uma distância segura.

2. Monitoramento de Aceleração:

- O MPU6050 é utilizado para medir a aceleração nas três dimensões (X, Y, Z).
Com base na magnitude da aceleração medida, o sistema pode detectar:
- Distância Segura: Aceleração abaixo de 0.3 g;
- Risco de Colisão: Aceleração entre 0.3 g e 1.0 g;
- Colisão Detectada: Aceleração acima de 1.5 g;

3. Exibição de Informações no LCD:

- Um LCD 16x2 exibe mensagens de status, como "Distância Segura", "Risco de Colisão!" e "Colisão!" conforme as condições detectadas pelo sistema.

4. Alerta Sonoro:

- O buzzer é utilizado para alertar o usuário quando uma proximidade perigosa é detectada ou quando uma colisão é iminente.

Itens Utilizados:

- Arduino Uno;
- Sensor Ultrassônico HC-SR04;
- MPU6050 (acelerômetro e giroscópio);
- Buzzer;
- LCD 16x2;
- Jumpers e cabos diversos.

Bibliotecas:

- Wire.h;
- MPU6050.h;
- LiquidCrystal.

Montagem: 

1. Montagem do Circuito:

Conecte o sensor ultrassônico HC-SR04 aos pinos adequados do Arduino (trigPin e echoPin);
Conecte o MPU6050 ao Arduino via I2C;
Conecte o buzzer aos pinos definidos no código (buzzerPin);
Conecte o LCD aos pinos definidos (RS, E, D4, D5, D6, D7).

2. Upload do Código:

Carregue o código fornecido para o Arduino usando a IDE Arduino ou uma plataforma de simulação como o Wokwi.

3. Verificação e Testes:

Verifique as conexões e execute o sistema;
Observe as mensagens exibidas no LCD e o comportamento do buzzer conforme a proximidade de obstáculos e a detecção de aceleração.

Instruções de Uso: 
- Ajustar a distância do sensor e aceleração de X, Y ou Z.

Código Fonte:

```c++
#include <Wire.h>
#include <MPU6050.h>
#include <LiquidCrystal.h>

const int trigPin = 12; // Pino TRIG do sensor HC-SR04
const int echoPin = 11; // Pino ECHO do sensor HC-SR04
const int buzzerPin = 8; // Pino do buzzer

// Define os valores de aceleração para cada estado
float accelThresholdSeguro = 0.3;   // Limite de aceleração para estado seguro (menor que 0.3 g)
float accelThresholdRisco = 1.0;    // Limite de aceleração para estado de risco (entre 0.3 g e 1.0 g)
float accelThresholdColisao = 1.5;  // Limite de aceleração para detecção de colisão (maior que 1.0 g)

MPU6050 mpu;
LiquidCrystal lcd(13, 10, 5, 4, 3, 2); // Define os pinos do LCD

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);

  lcd.begin(16, 2); // Inicializa o LCD com 16 colunas e 2 linhas

  Wire.begin();
  mpu.initialize();

  if (mpu.testConnection()) {
    Serial.println("MPU6050 conectado!");
  } else {
    Serial.println("Falha na conexao do MPU6050");
  }

  lcd.print("Distancia Segura"); // Mensagem inicial no LCD
}

void loop() {
  // Mede a distância com o sensor ultrassônico
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  // Lê os valores de aceleração do MPU6050
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  // Converte os valores para G-força
  float accelX = ax / 16384.0;
  float accelY = ay / 16384.0;
  float accelZ = az / 16384.0;

  // Calcula a magnitude da aceleração
  float accelMagnitude = sqrt(accelX * accelX + accelY * accelY + accelZ * accelZ);

  // Verifica o estado com base na aceleração medida
  if (accelMagnitude > accelThresholdColisao) {
    // Colisão detectada
    // Limpa o LCD e exibe mensagem de colisão
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Colisao!");

    // Ativa o buzzer
    digitalWrite(buzzerPin, HIGH);
  }  else {
    // Estado seguro
    // Limpa o LCD e exibe mensagem de distância segura
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Distancia Segura");

    // Verifica se a distância medida está menor que 20 cm
    if (distance < 50) {
      // Exibe "Colisao!" no LCD e ativa o buzzer
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Risco de colisao");
      digitalWrite(buzzerPin, HIGH);
      digitalWrite(buzzerPin, LOW);

    
    }
  }

  delay(100); // Aguarda para a próxima leitura
}
```
Link Wokwi: 

[https://wokwi.com/projects/400993835171468289]


