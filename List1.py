l = [ i for i in range(1,11)]
r=l[:5]
print(l)
print(f"Extracted first five elements: {r}")
r.sort(reverse = True)
print(f'Reversed extracted elements: {r}')
