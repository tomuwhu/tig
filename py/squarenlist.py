def f( a ):
    return a ** 2
print( * map( f, range( 20 ) ) )

print( * [ ( i, i ** 2 ) for i in range( 1, 15 ) ] )
