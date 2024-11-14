import unicodedata
def find_zero_width_characters(text):
    zero_width_chars = []
    for char in text:
        # Check if the character's Unicode category is 'Cf' (Format characters, including zero-width characters)
        if unicodedata.category(char) == 'Cf':
            zero_width_chars.append(char)
    return zero_width_chars
<!-- Flag: CyberTrail{h1dd3n_fl4g_1n_c0mm3nt} -->
# Example usage
input_text = """All our dreams can come true if we have the courage to pursue them	       
       		    	      		      	  	      	 	    
  	      			     	     	  	   	  	      
    			 	    	    	 	 	     	     
    	    		   		      	 	      	    	  
 		  	    	 	 	      	  	  	      
 	      	    	  	       	     	 	       		      
		  	       	   	       		  	  	     
	    	  	    	      	   		      	     
	     	  
"""  # Text with some zero-width characters

# Find and display zero-width characters in the input string
zero_width_chars = find_zero_width_characters(input_text)
print(zero_width_chars)