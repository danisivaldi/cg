for alg in {1..3}
do
	for op in {1..15}
	do
	python3 trab1.py < testes/test$alg$op.txt > times/time$alg$op.txt
	done
done