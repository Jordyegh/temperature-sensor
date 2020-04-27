import Adafruit_DHT

humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 6)

humidity = round(humidity, 2)
temperature = round(temperature, 2)

def updatePrints():
  if temperature is not None and humidity is not None:
    print 'Temperatuur: {0:0.1f}*C'.format(temperature)
    print 'Luchtvochtigheid: {0:0.1f}%'.format(humidity)
  else:
    print 'Geen data ontvangen op dit moment'
    
while true:
  updatePrints()
  time.sleep(10)
