def clean_mongo(doc):
    if isinstance(doc, list):
        return [clean_mongo(d) for d in doc]
    if isinstance(doc, dict):
        doc.pop("_id", None)
        return doc
    return doc