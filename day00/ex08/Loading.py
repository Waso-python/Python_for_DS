def ft_tqdm(lst: range) -> None:
    """
    Simple implementation of a progress bar similar to tqdm.
    Does not use external imports.
    """
    total = len(lst)
    
    for i, item in enumerate(lst, 1):
        # Calculate the percentage of completion
        percentage = (i / total) * 100
        
        # Calculate the number of filled blocks of the progress bar
        bar_length = 42  # Length as in the original tqdm
        filled_length = int(bar_length * i / total)
	
        # Create a progress bar with the █ symbol
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        
        # Form the progress string
        progress_str = f"\r{percentage:3.0f}%|{bar}| {i}/{total}"
        
        # Print the progress
        print(progress_str, end='', flush=True)
        
        yield item
