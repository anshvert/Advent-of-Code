use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt");
    match contents {
        Ok(contents) => {
            let trimmed = contents.trim();
            get_total_score(trimmed);
            get_total_score_part2(trimmed);
        }
        Err(e) => eprintln!("Error: {:?}", e),
    }
}

fn get_total_score(contents: &str) {
    let mut total_sum: u32 = 0;
    for (ind, _) in contents.chars().enumerate() {
        let next_index = (ind + 1) % contents.len();
        let curr = &contents[ind..ind + 1];
        let next = &contents[next_index..next_index + 1];
        if curr == next {
            total_sum += curr.parse::<u32>().unwrap();
        }
    }
    println!("Total Sum Part 1 {}", total_sum);
}

fn get_total_score_part2(contents: &str) {
    let mut total_sum: u32 = 0;
    let contents_length_half = contents.len() / 2;
    for index in 0..contents_length_half {
        let curr = &contents[index..index + 1];
        let next = &contents[index + contents_length_half..index + contents_length_half + 1];
        if curr == next {
            total_sum += curr.parse::<u32>().unwrap();
        }
    }
    println!("Total Sum Part 2 {}", total_sum * 2);
}
