#define crypto_stream_PRIMITIVE "xsalsa20"
#define crypto_stream crypto_stream_xsalsa20
#define crypto_stream_xor crypto_stream_xsalsa20_xor
#define crypto_stream_KEYBYTES crypto_stream_xsalsa20_KEYBYTES
#define crypto_stream_NONCEBYTES crypto_stream_xsalsa20_NONCEBYTES
#define crypto_stream_IMPLEMENTATION crypto_stream_xsalsa20_IMPLEMENTATION
#define crypto_stream_VERSION crypto_stream_xsalsa20_VERSION
#define crypto_stream_xsalsa20_tweet_KEYBYTES 32
#define crypto_stream_xsalsa20_tweet_NONCEBYTES 24
#define crypto_stream_xsalsa20_tweet_VERSION "-"
#define crypto_stream_xsalsa20 crypto_stream_xsalsa20_tweet
#define crypto_stream_xsalsa20_xor crypto_stream_xsalsa20_tweet_xor
#define crypto_stream_xsalsa20_KEYBYTES crypto_stream_xsalsa20_tweet_KEYBYTES
#define crypto_stream_xsalsa20_NONCEBYTES crypto_stream_xsalsa20_tweet_NONCEBYTES
#define crypto_stream_xsalsa20_VERSION crypto_stream_xsalsa20_tweet_VERSION
#define crypto_stream_xsalsa20_IMPLEMENTATION "crypto_stream/xsalsa20/tweet"
#define crypto_stream_salsa20_tweet_KEYBYTES 32
#define crypto_stream_salsa20_tweet_NONCEBYTES 8
#define crypto_stream_salsa20_tweet_VERSION "-"
#define crypto_stream_salsa20 crypto_stream_salsa20_tweet
#define crypto_stream_salsa20_xor crypto_stream_salsa20_tweet_xor
#define crypto_stream_salsa20_KEYBYTES crypto_stream_salsa20_tweet_KEYBYTES
#define crypto_stream_salsa20_NONCEBYTES crypto_stream_salsa20_tweet_NONCEBYTES
#define crypto_stream_salsa20_VERSION crypto_stream_salsa20_tweet_VERSION
#define crypto_stream_salsa20_IMPLEMENTATION "crypto_stream/salsa20/tweet"

# extern int crypto_stream_xsalsa20_tweet(unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);
# extern int crypto_stream_xsalsa20_tweet_xor(unsigned char *,const unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);
# extern int crypto_stream_salsa20_tweet(unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);
# extern int crypto_stream_salsa20_tweet_xor(unsigned char *,const unsigned char *,unsigned long long,const unsigned char *,const unsigned char *);
