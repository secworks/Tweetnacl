
# TweetNaCl auth defines.
#define crypto_auth_PRIMITIVE "hmacsha512256"
#define crypto_auth crypto_auth_hmacsha512256
#define crypto_auth_verify crypto_auth_hmacsha512256_verify
#define crypto_auth_BYTES crypto_auth_hmacsha512256_BYTES
#define crypto_auth_KEYBYTES crypto_auth_hmacsha512256_KEYBYTES
#define crypto_auth_IMPLEMENTATION crypto_auth_hmacsha512256_IMPLEMENTATION
#define crypto_auth_VERSION crypto_auth_hmacsha512256_VERSION
#define crypto_auth_hmacsha512256_tweet_BYTES 32
#define crypto_auth_hmacsha512256_tweet_KEYBYTES 32
#define crypto_auth_hmacsha512256_tweet_VERSION "-"
#define crypto_auth_hmacsha512256 crypto_auth_hmacsha512256_tweet
#define crypto_auth_hmacsha512256_verify crypto_auth_hmacsha512256_tweet_verify
#define crypto_auth_hmacsha512256_BYTES crypto_auth_hmacsha512256_tweet_BYTES
#define crypto_auth_hmacsha512256_KEYBYTES crypto_auth_hmacsha512256_tweet_KEYBYTES
#define crypto_auth_hmacsha512256_VERSION crypto_auth_hmacsha512256_tweet_VERSION
#define crypto_auth_hmacsha512256_IMPLEMENTATION "crypto_auth/hmacsha512256/tweet"

# TweetNaCl auth functions.
# extern int crypto_auth_hmacsha512256_tweet(unsigned char *,const unsigned char *,unsigned long long,const unsigned char *);
# extern int crypto_auth_hmacsha512256_tweet_verify(const unsigned char *,const unsigned char *,unsigned long long,const unsigned char *);
