def label_mode(method):
    method = method.lower()
    if "scratch" in method or "random" in method:
        return "reset"
    if "prun" in method or "revision" in method:
        return "revision"
    return "observe"
