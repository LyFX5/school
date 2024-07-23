package common;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.function.ToDoubleFunction;

public class ErrorLoggingFunction<T> implements ToDoubleFunction<T> {

	public final ToDoubleFunction<T> function;
	public final ConcurrentLinkedQueue<Double> log = new ConcurrentLinkedQueue<>();

	public ErrorLoggingFunction(ToDoubleFunction<T> function) {
		this.function = function;
	}

	@Override
	public double applyAsDouble(T value) {
		double result = function.applyAsDouble(value);
		log.add(result);
		return result;
	}

}
