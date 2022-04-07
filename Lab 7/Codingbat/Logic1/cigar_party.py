def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars < 40:
      return False
    return True
  elif 40 <= cigars <= 60:
    return True
  return False