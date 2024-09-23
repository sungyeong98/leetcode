/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let log = {};

    return function(...args) {
        let key = String(args);
        if (key in log){
            return log[key];
        }
        let result = fn(...args);
        log[key]=result;
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */