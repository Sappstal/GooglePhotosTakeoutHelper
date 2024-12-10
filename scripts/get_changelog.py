at
# Find next "##" (previous version)
try:
    end = lines.index('\n## ', start)
except ValueError:
    # in case there is no previous version
    end = -1

print(lines[start:end].strip())
