def f( a ):
    return a ** 2
print( * map( f, range( 10 ) ) )

x = [ ( i, i ** 2 ) for i in range( 1, 10 ) ]
print( * x )
