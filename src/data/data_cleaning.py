import pandas as pd
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def normalize_url(url):
    """
    Normalize a single URL:
    - Strip whitespace
    - Lowercase the scheme and domain
    """
    if pd.isna(url) or url == "":
        return None
    
    url = str(url).strip()
    
    try:
        parsed = urlparse(url)
        scheme = parsed.scheme.lower() if parsed.scheme else ""
        netloc = parsed.netloc.lower() if parsed.netloc else ""
        path = parsed.path
        query = parsed.query
        fragment = parsed.fragment
        
        normalized = f"{scheme}://{netloc}{path}"
        if query:
            normalized += f"?{query}"
        if fragment:
            normalized += f"#{fragment}"
        
        return normalized
    except Exception as e:
        logger.warning(f"Error normalizing URL: {url} - {e}")
        return url


def clean_dataset(df):
    """
    Clean the dataset:
    1. Remove rows with missing URLs or labels
    2. Normalize all URLs
    3. Return cleaned dataframe
    """
    logger.info(f"Starting with {len(df)} rows")
    
    df_clean = df.dropna(subset=["url", "label"])
    df_clean = df_clean[df_clean["url"].astype(str).str.strip() != ""]
    
    logger.info(f"After removing missing values: {len(df_clean)} rows")
    
    df_clean["url"] = df_clean["url"].apply(normalize_url)
    df_clean = df_clean[df_clean["url"].notna()]
    
    logger.info(f"After URL normalization: {len(df_clean)} rows")
    
    df_clean = df_clean.reset_index(drop=True)
    
    return df_clean