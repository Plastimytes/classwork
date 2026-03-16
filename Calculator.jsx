import { useState, useEffect, useCallback } from "react";

// ── Styles ────────────────────────────────────────────────────────────────────
const styles = `
  @import url('https://fonts.googleapis.com/css2?family=Syne+Mono&family=DM+Sans:wght@300;400;500&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0e0e10;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    font-family: 'DM Sans', sans-serif;
  }

  :root {
    --bg-shell:    #18181c;
    --bg-display:  #0e0e10;
    --bg-btn:      #232329;
    --bg-op:       #2e2e38;
    --bg-accent:   #c8f135;
    --bg-eq:       #c8f135;
    --txt-primary: #f0f0f0;
    --txt-dim:     #666;
    --txt-dark:    #0e0e10;
    --accent:      #c8f135;
    --radius:      20px;
    --btn-radius:  14px;
    --gap:         10px;
  }

  .shell {
    background: var(--bg-shell);
    border-radius: var(--radius);
    padding: 24px;
    width: 340px;
    box-shadow:
      0 40px 80px rgba(0,0,0,0.7),
      0 0 0 1px rgba(255,255,255,0.05),
      inset 0 1px 0 rgba(255,255,255,0.08);
    animation: rise 0.5s cubic-bezier(0.16,1,0.3,1);
  }

  @keyframes rise {
    from { opacity: 0; transform: translateY(30px) scale(0.96); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
  }

  /* ── Display ── */
  .display {
    background: var(--bg-display);
    border-radius: 12px;
    padding: 20px 20px 14px;
    margin-bottom: 20px;
    min-height: 110px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.04);
    position: relative;
  }

  .display-expr {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: var(--txt-dim);
    min-height: 18px;
    margin-bottom: 6px;
    letter-spacing: 0.02em;
    transition: all 0.2s;
    text-align: right;
    word-break: break-all;
    max-width: 100%;
  }

  .display-main {
    font-family: 'Syne Mono', monospace;
    font-size: 48px;
    color: var(--txt-primary);
    line-height: 1;
    letter-spacing: -1px;
    transition: font-size 0.15s;
    word-break: break-all;
    text-align: right;
    max-width: 100%;
  }

  .display-main.shrink   { font-size: 32px; }
  .display-main.shrink2  { font-size: 24px; }

  .display-main.pop {
    animation: pop 0.18s ease;
  }
  @keyframes pop {
    0%   { transform: scale(1); }
    40%  { transform: scale(1.04); }
    100% { transform: scale(1); }
  }

  /* ── Grid ── */
  .grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--gap);
  }

  /* ── Buttons ── */
  .btn {
    height: 68px;
    border: none;
    border-radius: var(--btn-radius);
    cursor: pointer;
    font-size: 18px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    transition:
      transform 0.1s,
      background 0.15s,
      box-shadow 0.15s;
    position: relative;
    overflow: hidden;
    outline: none;
    -webkit-tap-highlight-color: transparent;
  }

  .btn::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: rgba(255,255,255,0);
    transition: background 0.15s;
  }

  .btn:hover::after  { background: rgba(255,255,255,0.06); }
  .btn:active        { transform: scale(0.93); }
  .btn:active::after { background: rgba(255,255,255,0.12); }

  /* number */
  .btn-num {
    background: var(--bg-btn);
    color: var(--txt-primary);
    box-shadow: 0 2px 0 rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
  }
  .btn-num:hover { background: #2a2a32; }

  /* operator */
  .btn-op {
    background: var(--bg-op);
    color: var(--accent);
    font-size: 22px;
    box-shadow: 0 2px 0 rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
  }
  .btn-op:hover { background: #35353f; }

  /* function (AC, +/-, %) */
  .btn-fn {
    background: #2c2c34;
    color: #aaa;
    box-shadow: 0 2px 0 rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
  }
  .btn-fn:hover { background: #34343e; }

  /* equals */
  .btn-eq {
    background: var(--bg-eq);
    color: var(--txt-dark);
    font-size: 26px;
    font-weight: 600;
    box-shadow: 0 4px 0 #8aaa00, inset 0 1px 0 rgba(255,255,255,0.3);
  }
  .btn-eq:hover { background: #d4ff3d; }
  .btn-eq:active { box-shadow: 0 1px 0 #8aaa00; transform: scale(0.93) translateY(2px); }

  /* zero spans 2 cols */
  .btn-zero {
    grid-column: span 2;
    justify-content: flex-start;
    padding-left: 26px;
    display: flex;
    align-items: center;
    font-family: 'Syne Mono', monospace;
  }

  /* active operator highlight */
  .btn-op.active-op {
    background: #3a3a48;
    box-shadow: 0 0 0 1.5px var(--accent), 0 2px 0 rgba(0,0,0,0.4);
  }

  /* label */
  .label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--txt-dim);
    text-align: center;
    margin-bottom: 14px;
  }

  /* error flash */
  .display.error .display-main {
    color: #ff6b6b;
    animation: shake 0.3s ease;
  }
  @keyframes shake {
    0%,100% { transform: translateX(0); }
    20%      { transform: translateX(-6px); }
    60%      { transform: translateX(6px); }
  }
`;

// ── Helpers ───────────────────────────────────────────────────────────────────
const MAX_DIGITS = 12;

function fmt(val) {
  if (val === "Error") return "Error";
  const n = parseFloat(val);
  if (isNaN(n)) return val;
  if (Math.abs(n) >= 1e12 || (Math.abs(n) < 1e-6 && n !== 0)) {
    return n.toExponential(4);
  }
  const s = parseFloat(n.toPrecision(10)).toString();
  return s;
}

function calc(a, op, b) {
  const x = parseFloat(a), y = parseFloat(b);
  if (isNaN(x) || isNaN(y)) return "Error";
  switch (op) {
    case "+": return fmt(x + y);
    case "−": return fmt(x - y);
    case "×": return fmt(x * y);
    case "÷": return y === 0 ? "Error" : fmt(x / y);
    default: return b;
  }
}

// ── Component: Button ─────────────────────────────────────────────────────────
function CalcButton({ label, type = "num", onClick, wide, activeOp }) {
  const cls = [
    "btn",
    type === "op"  ? "btn-op"  : "",
    type === "fn"  ? "btn-fn"  : "",
    type === "eq"  ? "btn-eq"  : "",
    type === "num" ? "btn-num" : "",
    wide           ? "btn-zero": "",
    activeOp && type === "op" ? "active-op" : "",
  ].filter(Boolean).join(" ");

  return (
    <button className={cls} onClick={() => onClick(label)}>
      {label}
    </button>
  );
}

// ── Component: Display ────────────────────────────────────────────────────────
function Display({ main, expr, error, popping }) {
  const len = main.length;
  const sizeClass = len > 12 ? "shrink2" : len > 8 ? "shrink" : "";
  return (
    <div className={`display${error ? " error" : ""}`}>
      <div className="display-expr">{expr || "\u00A0"}</div>
      <div className={`display-main ${sizeClass} ${popping ? "pop" : ""}`}>
        {main}
      </div>
    </div>
  );
}

// ── Main App ──────────────────────────────────────────────────────────────────
export default function Calculator() {
  const [current, setCurrent]   = useState("0");
  const [prev, setPrev]         = useState(null);
  const [op, setOp]             = useState(null);
  const [expr, setExpr]         = useState("");
  const [justEvaled, setJustEvaled] = useState(false);
  const [error, setError]       = useState(false);
  const [popping, setPopping]   = useState(false);

  const triggerPop = () => {
    setPopping(false);
    requestAnimationFrame(() => setPopping(true));
  };

  // ── Input digit / decimal ──
  const inputDigit = useCallback((digit) => {
    setError(false);
    if (justEvaled) {
      setCurrent(digit === "." ? "0." : digit);
      setJustEvaled(false);
      return;
    }
    setCurrent(prev => {
      if (digit === ".") {
        return prev.includes(".") ? prev : prev + ".";
      }
      if (prev === "0") return digit;
      if (prev.length >= MAX_DIGITS) return prev;
      return prev + digit;
    });
  }, [justEvaled]);

  // ── Operator ──
  const inputOp = useCallback((nextOp) => {
    setError(false);
    setJustEvaled(false);
    if (op && prev !== null && !justEvaled) {
      const result = calc(prev, op, current);
      if (result === "Error") { setError(true); setCurrent("Error"); setOp(null); setPrev(null); setExpr(""); return; }
      setPrev(result);
      setCurrent(result);
      setExpr(`${result} ${nextOp}`);
      triggerPop();
    } else {
      setPrev(current);
      setExpr(`${current} ${nextOp}`);
    }
    setOp(nextOp);
    setJustEvaled(false);
  }, [op, prev, current, justEvaled]);

  // ── Equals ──
  const evaluate = useCallback(() => {
    if (!op || prev === null) return;
    const result = calc(prev, op, current);
    setExpr(`${prev} ${op} ${current} =`);
    if (result === "Error") {
      setError(true);
      setCurrent("Error");
    } else {
      setCurrent(result);
      triggerPop();
    }
    setPrev(null);
    setOp(null);
    setJustEvaled(true);
  }, [op, prev, current]);

  // ── AC ──
  const clear = useCallback(() => {
    setCurrent("0"); setPrev(null); setOp(null);
    setExpr(""); setJustEvaled(false); setError(false);
  }, []);

  // ── +/- ──
  const toggleSign = useCallback(() => {
    setCurrent(v => v === "0" || v === "Error" ? v : (v.startsWith("-") ? v.slice(1) : "-" + v));
  }, []);

  // ── % ──
  const percent = useCallback(() => {
    setCurrent(v => fmt(parseFloat(v) / 100));
  }, []);

  // ── Keyboard support ──
  useEffect(() => {
    const handler = (e) => {
      if (e.key >= "0" && e.key <= "9") inputDigit(e.key);
      else if (e.key === ".") inputDigit(".");
      else if (e.key === "+" ) inputOp("+");
      else if (e.key === "-" ) inputOp("−");
      else if (e.key === "*" ) inputOp("×");
      else if (e.key === "/" ) { e.preventDefault(); inputOp("÷"); }
      else if (e.key === "Enter" || e.key === "=") evaluate();
      else if (e.key === "Backspace") setCurrent(v => v.length > 1 ? v.slice(0,-1) : "0");
      else if (e.key === "Escape") clear();
      else if (e.key === "%") percent();
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, [inputDigit, inputOp, evaluate, clear, percent]);

  // ── Handle button press ──
  const handlePress = (label) => {
    if (label === "AC")  return clear();
    if (label === "+/−") return toggleSign();
    if (label === "%")   return percent();
    if (["+","−","×","÷"].includes(label)) return inputOp(label);
    if (label === "=")   return evaluate();
    inputDigit(label);
  };

  // ── Button layout ──
  const buttons = [
    { label:"AC",  type:"fn"  },
    { label:"+/−", type:"fn"  },
    { label:"%",   type:"fn"  },
    { label:"÷",   type:"op"  },
    { label:"7",   type:"num" },
    { label:"8",   type:"num" },
    { label:"9",   type:"num" },
    { label:"×",   type:"op"  },
    { label:"4",   type:"num" },
    { label:"5",   type:"num" },
    { label:"6",   type:"num" },
    { label:"−",   type:"op"  },
    { label:"1",   type:"num" },
    { label:"2",   type:"num" },
    { label:"3",   type:"num" },
    { label:"+",   type:"op"  },
    { label:"0",   type:"num", wide: true },
    { label:".",   type:"num" },
    { label:"=",   type:"eq"  },
  ];

  return (
    <>
      <style>{styles}</style>
      <div className="shell">
        <p className="label">Calculator</p>
        <Display
          main={current}
          expr={expr}
          error={error}
          popping={popping}
        />
        <div className="grid">
          {buttons.map(({ label, type, wide }) => (
            <CalcButton
              key={label}
              label={label}
              type={type}
              wide={wide}
              activeOp={op === label}
              onClick={handlePress}
            />
          ))}
        </div>
      </div>
    </>
  );
}
