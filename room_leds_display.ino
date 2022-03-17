#include <Adafruit_NeoPixel.h>

#define LED_PIN   6  // any PWM capable pin
#define NUM_LEDS 150

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_RGBW + NEO_KHZ800);

void setup()
{
  strip.begin();
  strip.setBrightness(100); // set brightness to n%
}

void loop()
{
  showMeteorPixels(1, 10, strip.Color(0, 150, 0));
  showMeteorPixels(1, 10, strip.Color(150, 0, 0));
  showMeteorPixels(1, 10, strip.Color(0, 0, 150));
  showMeteorPixels(1, 10, strip.Color(150, 150, 0));
  showMeteorPixels(1, 10, strip.Color(0, 150, 150));
  showMeteorPixels(1, 10, strip.Color(150, 0, 150));
  showMeteorPixels(1, 10, strip.Color(150, 150, 150));
}

void showMeteorPixels(int iterations, int delayMilliseconds, uint32_t color)
{
    const byte STEP = 1;
    uint8_t r, g, b;
    uint32_t col;
    unsigned long sum = 0;

    turnOffPixels();

    for (int iter = 0; iter < iterations; iter++) {
        byte headIndex = 0;
        do {
            sum = 0;

            for (byte i = 0; i < NUM_LEDS; i++) {
                col = strip.getPixelColor(i);
                sum += col;

                r = col >> 16;
                g = col >> 8;
                b = col;

                if (r > 0) {
                    r -= STEP;
                    r = max(0, r);
                }
                if (g > 0) {
                    g -= STEP;
                    g = max(0, g);
                }
                if (b > 0) {
                    b -= STEP;
                    b = max(0, b);
                }
                strip.setPixelColor(i, strip.Color(r, g, b));
            }

            if (headIndex < NUM_LEDS) {
                strip.setPixelColor(headIndex++, color);
                sum += color;
            }

            strip.show();
           
        } while (sum > 0);
    }
}

/*
 * sets strip color to 000 (off)
 */
void turnOffPixels()
{
  for (byte i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, strip.Color(0, 0, 0));
  }
  strip.show();
}

/*
 * sets strip color based on parameter
 */
void turnOnPixels(uint32_t color)
{
  turnOffPixels();
  
  for (byte i = 0; i < NUM_LEDS; i++) {
      strip.setPixelColor(i, color);
  }
  strip.show();
}
