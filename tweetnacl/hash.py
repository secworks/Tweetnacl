#define crypto_hash_PRIMITIVE "sha512"
#define crypto_hash crypto_hash_sha512
#define crypto_hash_BYTES crypto_hash_sha512_BYTES
#define crypto_hash_IMPLEMENTATION crypto_hash_sha512_IMPLEMENTATION
#define crypto_hash_VERSION crypto_hash_sha512_VERSION
#define crypto_hash_sha512_tweet_BYTES 64
#define crypto_hash_sha512_tweet_VERSION "-"
#define crypto_hash_sha512 crypto_hash_sha512_tweet
#define crypto_hash_sha512_BYTES crypto_hash_sha512_tweet_BYTES
#define crypto_hash_sha512_VERSION crypto_hash_sha512_tweet_VERSION
#define crypto_hash_sha512_IMPLEMENTATION "crypto_hash/sha512/tweet"
#define crypto_hash_sha256_tweet_BYTES 32
#define crypto_hash_sha256_tweet_VERSION "-"
#define crypto_hash_sha256 crypto_hash_sha256_tweet
#define crypto_hash_sha256_BYTES crypto_hash_sha256_tweet_BYTES
#define crypto_hash_sha256_VERSION crypto_hash_sha256_tweet_VERSION
#define crypto_hash_sha256_IMPLEMENTATION "crypto_hash/sha256/tweet"

# extern int crypto_hash_sha512_tweet(unsigned char *,const unsigned char *,unsigned long long);
# extern int crypto_hash_sha256_tweet(unsigned char *,const unsigned char *,unsigned long long);
