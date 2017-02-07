#define crypto_core_PRIMITIVE "salsa20"
#define crypto_core crypto_core_salsa20
#define crypto_core_OUTPUTBYTES crypto_core_salsa20_OUTPUTBYTES
#define crypto_core_INPUTBYTES crypto_core_salsa20_INPUTBYTES
#define crypto_core_KEYBYTES crypto_core_salsa20_KEYBYTES
#define crypto_core_CONSTBYTES crypto_core_salsa20_CONSTBYTES
#define crypto_core_IMPLEMENTATION crypto_core_salsa20_IMPLEMENTATION
#define crypto_core_VERSION crypto_core_salsa20_VERSION
#define crypto_core_salsa20_tweet_OUTPUTBYTES 64
#define crypto_core_salsa20_tweet_INPUTBYTES 16
#define crypto_core_salsa20_tweet_KEYBYTES 32
#define crypto_core_salsa20_tweet_CONSTBYTES 16
#define crypto_core_salsa20_tweet_VERSION "-"
#define crypto_core_salsa20 crypto_core_salsa20_tweet
#define crypto_core_salsa20_OUTPUTBYTES crypto_core_salsa20_tweet_OUTPUTBYTES
#define crypto_core_salsa20_INPUTBYTES crypto_core_salsa20_tweet_INPUTBYTES
#define crypto_core_salsa20_KEYBYTES crypto_core_salsa20_tweet_KEYBYTES
#define crypto_core_salsa20_CONSTBYTES crypto_core_salsa20_tweet_CONSTBYTES
#define crypto_core_salsa20_VERSION crypto_core_salsa20_tweet_VERSION
#define crypto_core_salsa20_IMPLEMENTATION "crypto_core/salsa20/tweet"
#define crypto_core_hsalsa20_tweet_OUTPUTBYTES 32
#define crypto_core_hsalsa20_tweet_INPUTBYTES 16
#define crypto_core_hsalsa20_tweet_KEYBYTES 32
#define crypto_core_hsalsa20_tweet_CONSTBYTES 16
#define crypto_core_hsalsa20_tweet_VERSION "-"
#define crypto_core_hsalsa20 crypto_core_hsalsa20_tweet
#define crypto_core_hsalsa20_OUTPUTBYTES crypto_core_hsalsa20_tweet_OUTPUTBYTES
#define crypto_core_hsalsa20_INPUTBYTES crypto_core_hsalsa20_tweet_INPUTBYTES
#define crypto_core_hsalsa20_KEYBYTES crypto_core_hsalsa20_tweet_KEYBYTES
#define crypto_core_hsalsa20_CONSTBYTES crypto_core_hsalsa20_tweet_CONSTBYTES
#define crypto_core_hsalsa20_VERSION crypto_core_hsalsa20_tweet_VERSION
#define crypto_core_hsalsa20_IMPLEMENTATION "crypto_core/hsalsa20/tweet"

extern int crypto_core_salsa20_tweet(unsigned char *,const unsigned char *,const unsigned char *,const unsigned char *);
extern int crypto_core_hsalsa20_tweet(unsigned char *,const unsigned char *,const unsigned char *,const unsigned char *);